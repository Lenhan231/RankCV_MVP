import os
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

from app.schemas import InterviewQuestionsRequest
from app.gemini_client import generate_interview_questions
import json

def run_test():
    if not os.getenv("GEMINI_API_KEY"):
        print("Lỗi: Không tìm thấy GEMINI_API_KEY. Vui lòng thiết lập biến môi trường này hoặc tạo file .env")
        return

    cv_text = """
    John Doe
    Kinh nghiệm: 3 năm làm Backend Developer.
    Kỹ năng: Java, Spring Boot, Docker, RESTful API, PostgreSQL.
    Từng làm việc với hệ thống Microservices có lượng truy cập cao.
    """

    job_text = """
    Mô tả công việc: Backend Developer
    Yêu cầu kỹ năng: Java 11+, Spring Boot, kinh nghiệm với Docker và Kubernetes.
    Ưu tiên ứng viên có kiến thức về CI/CD và viết test tốt.
    """

    print("Đang tạo câu hỏi phỏng vấn theo văn hóa FPT...")
    req = InterviewQuestionsRequest(cv_text=cv_text, job_text=job_text)
    
    try:
        response = generate_interview_questions(req)
        print("\n=== KẾT QUẢ ===")
        print(response.model_dump_json(indent=2))
    except Exception as e:
        print(f"\nLỗi khi gọi API: {e}")

if __name__ == "__main__":
    run_test()
