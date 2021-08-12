import streamlit as st
from datetime import datetime
from style import change_background

#Print date and time
date_now = datetime.now()
dt_string = date_now.strftime("%d/%m/%Y %H:%M:%S")
st.markdown(dt_string)	

#Title
st.title('Hal İçin Checklist')

#Create counter and checkbox counter if not already created.
if "counter" not in st.session_state:
        st.session_state.counter = 0
if "boxes_now" not in st.session_state:
        st.session_state.boxes_now = 0

#Increases the number of videos watched today.
def increment_counter():
        st.session_state.counter += 30
#Calculates the current number of checkboxes
def calculate_boxes_now(x):
        st.session_state.boxes_now = x
#Checks clock for working hours.
def check_clock(date_now, counter):
    if date_now.hour >= 18:
        st.success('Paydos')
        counter = 0
        return counter
    else:
        return counter

#Create boxes and calculate how many boxes are checked.
check_1 = st.checkbox('İlk 30 videoyu tamamla!', value=False)
check_2 = st.checkbox('İkinci 30 videoyu tamamla!', value=False)
check_3 = st.checkbox('Üçüncü 30 videoyu tamamla!', value=False)
boxes = check_1 + check_2 + check_3

#check_clock() function
st.session_state.counter = check_clock(date_now, st.session_state.counter)

#Works only in working hours.
#Calculates the number of videos according to the checked box.
if date_now.hour < 18:
    if boxes == 1:
        if st.session_state.boxes_now > boxes:
            calculate_boxes_now(boxes)
        else:
            increment_counter()
            calculate_boxes_now(boxes)
    elif boxes == 2:
        if st.session_state.boxes_now > boxes:
            calculate_boxes_now(boxes)
        else:
            increment_counter()
            calculate_boxes_now(boxes)
    elif boxes == 3:
        if st.session_state.boxes_now > boxes:
            calculate_boxes_now(boxes)
        else:
            increment_counter()
            if date_now.hour < 18: #Gives a message about how long need to rest.
                st.success(f'Güzel. Saat sonuna kadar dinlenebilirsin.\nKalan süre: {60 - date_now.minute} dk.')
            st.balloons()
            calculate_boxes_now(boxes)
        
#Writes total amount of watched videos
st.write('Bugün izlenen video sayısı: ',st.session_state.counter)

#Yapılmayanlar                                                                Uncompleted
#üçünü tamamlayınca checklist sıfırlama butonu çıksın.                        Create reset button when three boxes checked.
#tarayıcı kapatıp açıldığı zaman kaldığı yerden devam etsin.                  Sould works when close the browser.
#dinlenme süresinin sonu için alarm ekle                                      Add alarm for ending of rest.

#Yapılanlar                                                                   Completed
#sadece üçünü tamamlayınca 'güzel' yazsın.                                    Write 'Good', when all boxes checked.
#üçü tamamlanınca gif göster. altında da yazı yazsın.                         Create a gif when all boxes checked.
#font, background, renk değişecek.                                            Background, colors, fonts can be changed.
#saat sonuna kadar dinlen yazdıktan sonra kalan dakikayı göster.              Give a message about how long need to rest
#Saat altıya gelince paydos mesajı yazsın. ve sıfırlansın.                    Write 'Let's call it a day!' when 6 o'clock and reset counter.
#sayfanın herhangi bir yerinde tam tarih yazsın.                              Write date and time
#türkçe olabilir.                                                             Change language from eng to tr.
