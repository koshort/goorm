# Goorm

A little word cloud generator in Python - Korean wrapper  
파이썬 워드 클라우드 라이브러리 한국어 wrapper goorm(구름)

## Koshort :purple_heart: KoNLPy
[KoNLPy와 Koshort의 통합이 진행되고 있습니다!](https://github.com/konlpy/konlpy/issues/202)

## Installation
```bash
pip install goorm
```

## Examples
```
python -m goorm.cli --imagefile=demo\template\cat.png --text=demo\text\cat.txt --korean
```

![cat](/demo/cat.png)  

```
python -m goorm.cli --imagefile=demo\template\apple.png --text=demo\text\food.txt --korean
```

![food](/demo/apple.png)  

[자세한 예제가 있는 원본 문서](https://github.com/amueller/word_cloud)
