---
layout: default
title: 홈
---

# 채용 공고 모음

주요 IT 기업의 최신 채용 정보를 확인하세요.

## Facebook
{% for post in site.job_postings %}
  {% if post.service == "facebook" %}
* [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%Y년 %m월 %d일" }}
  {% endif %}
{% endfor %}

## Google
{% for post in site.job_postings %}
  {% if post.service == "google" %}
* [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%Y년 %m월 %d일" }}
  {% endif %}
{% endfor %}

## X
{% for post in site.job_postings %}
  {% if post.service == "x" %}
* [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%Y년 %m월 %d일" }}
  {% endif %}
{% endfor %} 