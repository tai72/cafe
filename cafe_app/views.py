import logging
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ContactForm, CreateMenuForm
from .models import CafeMenu

# ロガーのインスタンス化
logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class MenuView(generic.TemplateView):
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = [
            {
                'name': 'ブレンドコーヒー', 
                'price': 420, 
                'description': '当店おすすめの一杯です。\n迷った場合はぜひこちらをご堪能ください。', 
                'img_path': 'brend-coffee.jpg'
            }, 
            {
                'name': 'カフェオレ', 
                'price': 500, 
                'description': '産地直送の贅沢ミルクを使用しています。\nオリジナルのラテアートも自慢です。', 
                'img_path': 'cafe-au-lait.jpg'
            }, 
            {
                'name': '紅茶', 
                'price': 480, 
                'description': '圧倒的な茶葉使用。\n\n故郷でもない外国の景色に想いを馳せることができます。', 
                'img_path': 'black-tea.jpg'
            }, 
        ]

        return context

class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('cafe_app:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'お問い合わせありがとうございます。')
        logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class OriginalMenuList(LoginRequiredMixin, generic.ListView):
    model = CafeMenu
    template_name = 'original_menu_list.html'

    def get_queryset(self):
        # ログインユーザーに基づいたメニューを抽出している.さらに作成日時の新しい順で.
        menus = CafeMenu.objects.filter(user=self.request.user).order_by('-created_at')
        return menus

class CreateMenuView(LoginRequiredMixin, generic.CreateView):
    model = CafeMenu
    template_name = 'create_menu.html'
    form_class = CreateMenuForm
    success_url = reverse_lazy('cafe_app:original_menu_list')

    # データベースに保存するだけなら不要だが、userやcreated_atなどがカスタムユーザーモデルからなのでオーバーライドする必要がある.
    def form_valid(self, form):
        menu = form.save(commit=False)
        menu.user = self.request.user
        menu.save()
        messages.success(self.request, '新規メニューを作成しました')
        return super().form_valid(form)

class MenuDetailView(LoginRequiredMixin, generic.DetailView):
    model = CafeMenu
    # slug_field = 'name'    # モデルのフィールド名
    # slug_url_kwarg = 'name'    # urls.pyでのキーワード名
    template_name = 'menu_detail.html'

class MenuUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CafeMenu
    template_name = 'menu_update.html'
    form_class = CreateMenuForm

    # URLが動的に変化するページに遷移する場合に用いる
    def get_success_url(self):
        return reverse_lazy('cafe_app:menu_detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        messages.success(self.request, 'メニューを更新しました')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'メニューの更新に失敗しました')
        return super().form_invalid(form)
        
class MenuDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CafeMenu
    template_name = 'menu_delete.html'
    success_url = reverse_lazy('cafe_app:original_menu_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'メニューを削除しました')
        return super().delete(request, *args, **kwargs)
