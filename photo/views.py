from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Photo

# 로그인한 사용자만 서비스를 사용할 수 있도록 권한 제안 (데코레이터와 믹스인 사용)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
# 사진 목록 만들기
def photo_list(request): #함수형 뷰 (클래스형 뷰와는 달리 모든 기능을 직접 처리해야 함)
    photos = Photo.objects.all() #DB에 저장된 모든 객체 불러오기
    return render(request, 'photo/list.html', {'photos':photos}) #렌더링


class PhotoUploadView(LoginRequiredMixin, CreateView): #사진 업로드
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form): #업로드 이후 이동할 페이지를 호출
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin, DeleteView): #사진 삭제
    model=Photo
    success_url='/'
    template_name='photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, UpdateView): #사진 수정
    model=Photo
    fields=['photo','text']
    template_name='photo/update.html'