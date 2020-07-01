package JC;

public class BrandTV extends TV {
    
    String brand;

    public BrandTV(int intValue, String strValue) {
        // 부모가 가지고 있는 channel 변수에 값을 할당한다.
        super.channel = intValue;
        this.brand = strValue;
    }

    public static void main(String args[]) {
        BrandTV objTV = new BrandTV(11, "삼성TV");
    //    objTV.channelUp();         // 접근 가능
        objTV.channelDown();       // 접근 불가능(컴파일 에러)
        System.out.println(objTV.brand + " 현재 채널은 " + objTV.channel + "번입니다.");
    }
}