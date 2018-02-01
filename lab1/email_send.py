from gmail import GMail, Message
from random import choice

html_template ='''
<p><span style="background-color: #ff0000;">Xin nghỉ ốm,</span></p>
<p>&nbsp;</p>
<p><strong>Thư xin nghỉ ngắn gọn v&agrave; s&uacute;c t&iacute;ch</strong></p>
<p>L&yacute; do: {{sickness}} </p>
<p>&nbsp;</p>
<p>Cho anh nghỉ.</p>
'''

sickness_list = ["dau bung", "ban viec", "ve que"]

sick = choice(sickness_list)
html_content = html_template.replace("{{sickness}}", sick)

gmail = GMail ('tailieu1234@gmail.com', 'tailieu56')
msg = Message('Xin chao Huy', to='c4e.201708@gmail.com',
    text='Anh Tuan test mail',html=html_content,
    attachments=['anhmail.png'])
gmail.send(msg)
