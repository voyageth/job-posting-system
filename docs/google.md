---
layout: default
title: Google 채용
---

<div class="company-section">
    <h1>Google 채용 정보</h1>
    <p>Google의 최신 채용 정보를 확인하세요.</p>

    <ul class="job-list">
    {% for post in site.job_postings %}
        {% if post.service == "google" %}
        <li>
            <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
            <p class="post-date">{{ post.date | date: "%Y년 %m월 %d일" }}</p>
            {% if post.team %}
            <p class="post-team">{{ post.team }}</p>
            {% endif %}
        </li>
        {% endif %}
    {% endfor %}
    </ul>
</div> 