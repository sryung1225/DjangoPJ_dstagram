from django.contrib import admin

from .models import Photo

#관리자 페이지 보기 좋게 커스터마이징
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated'] #목록이 보일 필드 설정
    raw_id_fields = ['author'] #검색 기능 사용 가능
    list_filter = ['created', 'updated', 'author'] #필터 기능을 사용할 필드 선택
    search_fields = ['text', 'created'] #검색 기능을 통해 검색할 필드를 선택
    ordering = ['-updated', '-created'] #기본 정렬값 설정

admin.site.register(Photo, PhotoAdmin)