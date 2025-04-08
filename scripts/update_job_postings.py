import os
import yaml
from openai import OpenAI
from pathlib import Path
import frontmatter
from datetime import datetime

# OpenAI API 설정
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_yaml_data(file_path):
    """YAML 파일에서 데이터를 로드합니다."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_job_posting(team_data):
    """LLM API를 사용하여 채용 공고를 생성합니다."""
    prompt = f"""
다음 정보를 바탕으로 매력적인 채용 공고를 작성해주세요:

팀: {team_data['team']}
기술 스택: {', '.join(team_data['tech_stack'])}
필수 요구사항: {', '.join(team_data['requirements'])}
이상적인 후보자: {', '.join(team_data['ideal_candidate'])}
프로젝트: {', '.join(team_data['projects'])}
문화: {', '.join(team_data['culture'])}

채용 공고는 다음 형식으로 작성해주세요:
1. 역할 소개
2. 주요 책임
3. 자격 요건
4. 우대사항
5. 회사 문화
6. 혜택
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 전문적인 채용 담당자입니다. 매력적이고 전문적인 채용 공고를 작성해주세요."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def save_job_posting(service_name, team_name, content):
    """생성된 채용 공고를 마크다운 파일로 저장합니다."""
    output_dir = Path("docs") / "_job-postings" / service_name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    post = {
        "title": f"{service_name} {team_name} 채용",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "service": service_name,
        "team": team_name,
        "layout": "post"
    }
    
    output_file = output_dir / f"{team_name.lower()}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(frontmatter.Post(content, **post)))

def main():
    """메인 실행 함수"""
    services_dir = Path("services")
    
    for service_path in services_dir.glob("*"):
        if not service_path.is_dir():
            continue
            
        service_name = service_path.name
        
        for team_file in service_path.glob("*.yaml"):
            team_name = team_file.stem.upper()
            team_data = load_yaml_data(team_file)
            
            try:
                job_posting = generate_job_posting(team_data)
                save_job_posting(service_name, team_name, job_posting)
                print(f"✅ {service_name} {team_name} 채용공고가 업데이트되었습니다.")
            except Exception as e:
                print(f"❌ {service_name} {team_name} 처리 중 오류 발생: {str(e)}")

if __name__ == "__main__":
    main() 