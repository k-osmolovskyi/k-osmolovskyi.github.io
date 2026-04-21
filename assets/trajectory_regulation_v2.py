import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + np.exp(-x))

def run_simulation_v2(
    input_series,
    R0=1.0,
    h=1.0,
    a=1.0,
    b=0.5,
    alpha=0.2,
    kT=2.2,
    kL=2.8,
    c=2.05,
    tau1=0.45,
    tau2=0.75,
    gamma=0.06,   # baseline resource recovery
    delta=0.10,   # resource depletion from pressure
    R_min=0.35,
    R_max=1.25,
):
    """
    Minimal demo trajectory-dependent regulation.
    V2
    - dynamic resource R_t
    - overload memory L_t
    - smooth behavioral output y_t = 1 - A_t
    """

    L = 0.0
    R = float(R0)

    records = {
        "t": [],
        "d": [],
        "T": [],
        "R": [],
        "theta": [],
        "u": [],
        "L": [],
        "A": [],
        "mode_num": [],
        "mode_name": [],
        "y": [],
    }

    for t, d in enumerate(input_series, start=1):
        T = float(d)
        theta = (a * R) / (1.0 + b * h)
        u = max(0.0, T - theta)
        A = sigmoid(kT * T + kL * L - c)

        if A < tau1:
            mode_name = "stable"
            mode_num = 0
        elif A < tau2:
            mode_name = "protective"
            mode_num = 1
        else:
            mode_name = "rigid"
            mode_num = 2

        y = max(0.0, min(1.0, 1.0 - A))

        records["t"].append(t)
        records["d"].append(d)
        records["T"].append(T)
        records["R"].append(R)
        records["theta"].append(theta)
        records["u"].append(u)
        records["L"].append(L)
        records["A"].append(A)
        records["mode_num"].append(mode_num)
        records["mode_name"].append(mode_name)
        records["y"].append(y)

        L = (1.0 - alpha) * L + u
        R = R + gamma - delta * T
        R = min(max(R, R_min), R_max)

    return records


trajectory_A = [0.20, 0.30, 0.35, 0.40, 0.45, 0.50, 0.60]
trajectory_B = [0.65, 0.78, 0.82, 0.74, 0.66, 0.55, 0.60]
trajectory_C = [0.95, 1.05, 1.10, 0.95, 0.85, 0.55, 0.60]

rec_A = run_simulation_v2(trajectory_A)
rec_B = run_simulation_v2(trajectory_B)
rec_C = run_simulation_v2(trajectory_C)

labels = [("A", rec_A), ("B", rec_B), ("C", rec_C)]
print("Final comparison at the same present input:")
for name, rec in labels:
    print(
        f"{name}: d={rec['d'][-1]:.2f}, "
        f"R={rec['R'][-1]:.3f}, "
        f"L={rec['L'][-1]:.3f}, "
        f"A={rec['A'][-1]:.3f}, "
        f"mode={rec['mode_name'][-1]}, "
        f"y={rec['y'][-1]:.3f}"
    )

plt.figure(figsize=(10, 4))
plt.plot(rec_A["t"], rec_A["d"], marker="o", label="Trajectory A")
plt.plot(rec_B["t"], rec_B["d"], marker="o", label="Trajectory B")
plt.plot(rec_C["t"], rec_C["d"], marker="o", label="Trajectory C")
plt.xlabel("Time step")
plt.ylabel("External pressure d_t")
plt.title("Version 2: External pressure trajectories")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(rec_A["t"], rec_A["R"], marker="o", label="Trajectory A")
plt.plot(rec_B["t"], rec_B["R"], marker="o", label="Trajectory B")
plt.plot(rec_C["t"], rec_C["R"], marker="o", label="Trajectory C")
plt.xlabel("Time step")
plt.ylabel("Resource R_t")
plt.title("Dynamic resource")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(rec_A["t"], rec_A["L"], marker="o", label="Trajectory A")
plt.plot(rec_B["t"], rec_B["L"], marker="o", label="Trajectory B")
plt.plot(rec_C["t"], rec_C["L"], marker="o", label="Trajectory C")
plt.xlabel("Time step")
plt.ylabel("Overload memory L_t")
plt.title("Trajectory-dependent overload memory")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(rec_A["t"], rec_A["A"], marker="o", label="Trajectory A")
plt.plot(rec_B["t"], rec_B["A"], marker="o", label="Trajectory B")
plt.plot(rec_C["t"], rec_C["A"], marker="o", label="Trajectory C")
plt.axhline(0.45, linestyle="--", label="tau1")
plt.axhline(0.75, linestyle="--", label="tau2")
plt.xlabel("Time step")
plt.ylabel("Admissibility pressure A_t")
plt.title("Admissibility score")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(rec_A["t"], rec_A["y"], marker="o", label="Trajectory A")
plt.plot(rec_B["t"], rec_B["y"], marker="o", label="Trajectory B")
plt.plot(rec_C["t"], rec_C["y"], marker="o", label="Trajectory C")
plt.xlabel("Time step")
plt.ylabel("Behavioral output y_t")
plt.title("Smooth behavioral consequence")
plt.legend()
plt.tight_layout()
plt.show()
