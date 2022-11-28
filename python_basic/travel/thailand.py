class TailandPackage:
  def detail(self):
    print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":
  print("Thaild 모듈 직접 실행")
  print("이 문장은 모듈을 직접 실행할때 실행")
  trip_to = TailandPackage()
  trip_to.detail()
else:
  print("Thailand 외부에서 모듈 호출")