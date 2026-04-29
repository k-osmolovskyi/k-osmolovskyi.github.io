---
layout: page
title: "Research Notes"
permalink: /notes/
---

Interim thoughts and comments.

<ul>
  {% for post in site.posts %}
    <li>
      <span style="color: #666;">{{ post.date | date: "%d.%m.%Y" }}</span> — 
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
