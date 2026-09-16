import pandas as pd

# 데이터프레임 생성
data = {
    '이름': ['김철수', '이영희', '박민수'],
    '나이': [25, 30, 22],
    '도시': ['서울', '부산', '대구']
}
df = pd.DataFrame(data)

# 데이터 확인 및 통계
print(df)
print(df['나이'].mean()) # 나이 평균 계산 (25.66...)
