```
=====================================================================
| 이 프로그램은 Cacti의 RRD TOOL을 이용해 계산을 하는 프로그램 입니다.  |
| PYTHONv2 를 이용하며 사용 방법은 아래를 참조하시면 됩니다.            |
| 반드시 날짜 포멧을 맞춰서 입력해야 하며, 한 달을 기준으로만 동작 합니다.|
=====================================================================
```


ex)
YYYY-MM-DD HH:MM:SS

1991-01-01 02:23:59 (o)
2008-19-01 24:59:59 (x)
2008 09 01 00: 00 : 00 (x)

( '-' 와 ':' 양식을 지켜야 하고, 시 분 초 까지 입력하여야 합니다.)

##### 띄워쓰기와 - 표와 : 표시를 확인하세요

=========================================================


코드 주석은 한글로 되어 잇다가, LINUX 서버의 UTF-8 encoding 문제로 인해,
영어로 주석을 단 상태입니다.

소스코드는 모두 공유이나,
RRD를 가져오는 파일은 수정하셔서 사용하여야 합니다.
