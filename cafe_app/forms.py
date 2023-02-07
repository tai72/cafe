from django import forms

class ContactForm(forms.Form):
    # フォーム項目のフィールドを作成
    name = forms.CharField(label='お名前', max_length=30, error_messages={'required': '必須項目です'})
    email = forms.EmailField(label='メールアドレス', error_messages={'required': '必須項目です'})
    tel = forms.CharField(label='電話番号', required=False)
    title = forms.CharField(label='タイトル', max_length=50, required=False)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 属性値の追加
        self.fields['name'].widget.attrs['placeholder'] = '例）じゃんご太郎'
        self.fields['email'].widget.attrs['placeholder'] = '例）django@django.co.jp'
        self.fields['tel'].widget.attrs['placeholder'] = '例）08012345678'
        self.fields['title'].widget.attrs['placeholder'] = '例）撮影許可のお願い'
        self.fields['message'].widget.attrs['placeholder'] = 'ここに本文を入力してください'
