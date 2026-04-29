---
layout: page
title: "Research Notes"
permalink: /notes/
---

Everything I wanted, and still want, to say precisely, concretely, and formally, I say through [my publications](https://zenodo.org/communities/gtc).

Here, I share notes and thoughts.

The form of these notes may be loose, non-literal, and of course sometimes mistaken in the moment. They should be treated as a flow of thought, not as fixed claims.

<ul>
  {% for post in site.posts %}
    <li>
      <span style="color: #666;">{{ post.date | date: "%d.%m.%Y" }}</span> — 
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
