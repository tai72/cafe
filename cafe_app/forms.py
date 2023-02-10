import os
import json
from pathlib import Path
from django import forms
from django.core.mail import EmailMessage

from .models import CafeMenu

# Read settings.json
BASE_DIR = Path(__file__).resolve().parent.parent
try:
    config_path = os.path.join(BASE_DIR, 'settings.json')
    config = json.load(open(config_path, "r", encoding="utf-8"))
except FileNotFoundError as e:
    print("[ERROR] Config file is not found.")
    raise e
except ValueError as e:
    print("[ERROR] Json file is invalid.")
    raise e

secret_key = config['SECRET_KEY']
email_host = config['EMAIL_HOST']
email_outlook = config['EMAIL_OUTLOOK']
email_host_pass = config['EMAIL_HOST_PASS']

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
    
    def send_email(self):
        # ユーザー入力値の取得
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        tel = self.cleaned_data['tel']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        # --- メール内容の設定 ---

        # 件名
        subject = f'[お問い合わせ]{title}'

        # 本文
        body = (
            'cefe_appにてお問い合わせがありました。\n\n' + 
            f'送信者: {name}\n' + 
            'メールアドレス:\n' + 
            f'{email}\n' + 
            f'電話番号: {tel}\n' + 
            'メッセージ\n' + 
            f'{message}'
        )

        # 送信元メールアドレス
        from_email = email_outlook

        # 送信先メールアドレス
        to_list = [email_outlook]

        # CCリスト
        cc_list = [email_outlook]

        # メール送信処理
        msg = EmailMessage(subject=subject, body=body, from_email=from_email, to=to_list, cc=cc_list)
        msg.send()

class CreateMenuForm(forms.ModelForm):
    class Meta:
        model = CafeMenu
        fields = ('photo', 'name', 'price', 'description')
