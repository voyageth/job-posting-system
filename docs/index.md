---
layout: default
title: 홈
---

<div class="company-section">
    <h1>채용 공고 모음</h1>
    <p>주요 IT 기업의 최신 채용 정보를 확인하세요.</p>

    <h2>Facebook</h2>
    <ul class="job-list">
    {% for post in site.job_postings %}
        {% if post.service == "facebook" %}
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

    <h2>Google</h2>
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

    <h2>X</h2>
    <ul class="job-list">
    {% for post in site.job_postings %}
        {% if post.service == "x" %}
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