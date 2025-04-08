# 채용 공고 자동화 시스템

이 프로젝트는 GitHub Pages와 LLM API를 활용하여 각 서비스별 채용 공고를 자동으로 관리하고 업데이트하는 시스템입니다.

## 프로젝트 구조

```
/
├── services/           # 서비스별 채용 정보
│   ├── facebook/      # Facebook 관련 정보
│   ├── google/        # Google 관련 정보
│   └── x/             # X(구 Twitter) 관련 정보
├── scripts/           # 자동화 스크립트
├── .github/           # GitHub Actions 설정
└── docs/             # 문서 및 GitHub Pages 소스
```

## 설정 방법

1. 리포지토리를 클론합니다
2. GitHub Secrets에 `LLM_API_KEY`를 설정합니다
3. GitHub Pages를 활성화합니다

## 사용 방법

1. `services` 디렉토리 내의 각 서비스 폴더에서 팀별 정보를 수정합니다
2. 변경사항을 커밋하면 자동으로 채용공고가 업데이트됩니다
3. GitHub Pages에서 최신 채용공고를 확인할 수 있습니다 