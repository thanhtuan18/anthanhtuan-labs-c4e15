from gmail import GMail, Message
from datetime import datetime

mail_content = """
<p><strong>Dear Mr./ Mrs.,</strong></p>
<p>I would like to request a leave of absence. </p>
<p><strong>Reason</strong>: <em>I'm sickness</em></p>
<p>Please let me know if I can provide any further information regarding this request.</p>
<p>Thank you very much for your consideration.</p>
<p>With kind regards,</p>
"""

gmail = GMail("tailieu1234", "tailieu56")
msg = Message("Notice from Tuan", to="anthanhtuan@gmail.com", html=mail_content)

times = datetime.now()
if times.hour >= 7:
    gmail.send(msg)
