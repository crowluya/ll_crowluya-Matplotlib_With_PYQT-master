# -*- encoding: utf-8 -*-
import os
from win32com import client


# pip instatll win32com
def doc2pdf(doc_name, pdf_name):
    """
    :word文件转pdf
    :param doc_name word文件名称
    :param pdf_name 转换后pdf文件名称
    """
    try:
        word = client.DispatchEx("Word.Application")
        if os.path.exists(pdf_name):
            os.remove(pdf_name)
        worddoc = word.Documents.Open(doc_name, ReadOnly=1)
        worddoc.SaveAs(pdf_name, FileFormat=17)
        worddoc.Close()
        return pdf_name
    except:
        print('出错啦')
        return 1


if __name__ == '__main__':
    doc_name = "data/test1.docx"
    ftp_name = "data/test1.pdf"
    doc2pdf(doc_name, ftp_name)
