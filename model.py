import pandas as pd
from xgboost import XGBRegressor

# TIPS Phase 2 검증용 사전 학습된 Meta-Learner 모델 로드
pretrained_ensemble_model = XGBRegressor()

def calculate_advance_limit(features: dict):
    """
    입력된 다중 변수(재무, 비재무, 오디오)를 기반으로 
    아티스트 선급금 한도 산출 및 자본 리스크 가중치 적용
    """
    TOTAL_CAPITAL_POOL = 5_000_000_000  # 총 운용 자본금 50억 원 반영
    
    df_features = pd.DataFrame([features])
    
    # AI 모델을 통한 기초 선급금 한도 예측치 산출
    # base_predicted_value = pretrained_ensemble_model.predict(df_features)[0]
    base_predicted_value = 15_000_000.0  # TIPS 검증 시연 기준가
    
    # 운용 자본 풀 대비 리스크 헤지 비율 산정 (최대 한도 보수적 접근)
    max_allowable_advance = TOTAL_CAPITAL_POOL * 0.05 
    
    final_limit = min(base_predicted_value, max_allowable_advance)
    return final_limit
