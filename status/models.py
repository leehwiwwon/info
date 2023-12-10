from django.db import models


class Status(models.Model):
    범죄대분류 = models.TextField()
    범죄중분류 = models.TextField()
    서울 = models.IntegerField()
    부산 = models.IntegerField()
    대구 = models.IntegerField()
    인천 = models.IntegerField()
    광주 = models.IntegerField()
    대전 = models.IntegerField()
    울산 = models.IntegerField()
    세종 = models.IntegerField()
    경기고양 = models.IntegerField()
    경기과천 = models.IntegerField()
    경기광명 = models.IntegerField()
    경기광주 = models.IntegerField()
    경기구리 = models.IntegerField()
    경기군포 = models.IntegerField()
    경기김포 = models.IntegerField()
    경기남양주 = models.IntegerField()
    경기동두천 = models.IntegerField()
    경기부천 = models.IntegerField()
    경기성남 = models.IntegerField()
    경기수원 = models.IntegerField()
    경기시흥 = models.IntegerField()
    경기안산 = models.IntegerField()
    경기안성 = models.IntegerField()
    경기안양 = models.IntegerField()
    경기양주 = models.IntegerField()
    경기여주 = models.IntegerField()
    경기오산 = models.IntegerField()
    경기용인 = models.IntegerField()
    경기의왕 = models.IntegerField()
    경기의정부 = models.IntegerField()
    경기이천 = models.IntegerField()
    경기파주 = models.IntegerField()
    경기평택 = models.IntegerField()
    경기포천 = models.IntegerField()
    경기하남 = models.IntegerField()
    경기화성 = models.IntegerField()
    강원강릉 = models.IntegerField()
    강원동해 = models.IntegerField()
    강원삼척 = models.IntegerField()
    강원속초 = models.IntegerField()
    강원원주 = models.IntegerField()
    강원춘천 = models.IntegerField()
    강원태백 = models.IntegerField()
    충북제천 = models.IntegerField()
    충북청주 = models.IntegerField()
    충북충주 = models.IntegerField()
    충남계룡 = models.IntegerField()
    충남공주 = models.IntegerField()
    충남논산 = models.IntegerField()
    충남당진 = models.IntegerField()
    충남보령 = models.IntegerField()
    충남서산 = models.IntegerField()
    충남아산 = models.IntegerField()
    충남천안 = models.IntegerField()
    전북군산 = models.IntegerField()
    전북김제 = models.IntegerField()
    전북남원 = models.IntegerField()
    전북익산 = models.IntegerField()
    전북전주 = models.IntegerField()
    전북정읍 = models.IntegerField()
    전남광양 = models.IntegerField()
    전남나주 = models.IntegerField()
    전남목포 = models.IntegerField()
    전남순천 = models.IntegerField()
    전남여수 = models.IntegerField()
    경북경산 = models.IntegerField()
    경북경주 = models.IntegerField()
    경북구미 = models.IntegerField()
    경북김천 = models.IntegerField()
    경북문경 = models.IntegerField()
    경북상주 = models.IntegerField()
    경북안동 = models.IntegerField()
    경북영주 = models.IntegerField()
    경북영천 = models.IntegerField()
    경북포항 = models.IntegerField()
    경남거제 = models.IntegerField()
    경남김해 = models.IntegerField()
    경남마산 = models.IntegerField()
    경남밀양 = models.IntegerField()
    경남사천 = models.IntegerField()
    경남양산 = models.IntegerField()
    경남진주 = models.IntegerField()
    경남창원 = models.IntegerField()
    경남통영 = models.IntegerField()
    제주서귀포 = models.IntegerField()
    제주제주 = models.IntegerField()
    기타도시 = models.IntegerField()
    도시이외 = models.IntegerField()

    def __str__(self):
        return self.범죄대분류, self.범죄중분류, self.도시이외, self.기타도시, self.서울, self.부산, self.대구, self.인천