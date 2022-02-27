from ssl import _create_default_https_context
import cv2
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="index.html"
    def get_context_data(self):
        ctxt=super().get_context_data()
        ctxt["username"]="佐藤"
        ctxt["num"]=123
        print(ctxt)
        return ctxt
#ここの部分はctxtじゃないとできないわけではない。
#おそらくsuperはtenplateviewのクラスにあるメソッドである。このメッソドの返り値は
#辞書型である.
"""このデータをhtmlで出力するには？
このデータはhtml上では辞書のkeyが変数名にvalueが値としてデータを渡しているので
html上に{{username}}と記述すればhtml上で出力できる"""
    
class AboutView(TemplateView):
    template_name="about.html"
    def get_context_data(self):
        ctxt=super().get_context_data()
        ctxt["skills"]=["python","java","go"]
        ctxt["num"]=123
        print(ctxt)
        return ctxt

    

