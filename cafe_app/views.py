from django.views import generic

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