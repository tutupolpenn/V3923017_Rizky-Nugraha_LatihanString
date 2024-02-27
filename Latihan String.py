#!/usr/bin/env python
# coding: utf-8

# In[16]:


nama_lengkap = input ("Masukkan Nama anda : ")

#Menghitung jumlah huruf dari nama lengkap
jumlah_huruf = len(nama_lengkap.replace(" ",""))

#menghitung jumlah huruf vokal dari nama lengkap
huruf_vokal = "aiueoAIUEO"
jumlah_vokal = len([char for char in nama_lengkap if huruf_vokal])

#menghitung jumlah huruf konsonan dari nama lengkap
jumlah_konsonan = jumlah_huruf - jumlah_vokal

print("jumlah huruf dari nama lengkap anda adalah :", jumlah_huruf)
print("jumlah huruf vokal dari nama lengkap anda adalah :", jumlah_vokal)
print("jumlah huruf konsonan dari nama lengkap anda adalah :", jumlah_konsonan)


# In[ ]:




