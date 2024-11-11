import subprocess
import time

test_cases = [
    "test_cases/test_case1.py"
]

for _ in range(1):
    for test_case in test_cases:
        try:
            print(f"{test_case} 실행중...")
            result = subprocess.run(["python", test_case], check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"{test_case} 실행 실패:", e)

        time.sleep(2)
