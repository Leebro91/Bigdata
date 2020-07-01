package JC;

public class TV {
     int channel;

    public TV() {}

    public TV(int intValue) {
        this.channel = intValue;
    }

    // 메소드의 접근 제한자를 protected로 변경
    protected void channelUp() {
        channel = channel + 1;
    }

    // 메소드의 접근 제한자를 private으로 변경
    private void channelDown() {
        channel = channel - 1;
        if (channel < 0) {
            channel = 0;
        }
    }

    public static void main(String args[]) {
        TV objTV = new TV(11);
        System.out.println("현재 채널은 " + objTV.channel + "번입니다.");
    }
}