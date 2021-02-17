# MovieCocktail API
MovieCocktail uygulamasının backend işlerini yapan flask ile yazılmış bir API.

* Procfile, heroku deployment için gereklidir. Flask API deploy etmek için bu dosyanın içeriği  "web gunicorn app:app" şeklinde olmalıdır. web ile gunicorn arasında ":" olmamalı!
* Gunicorn flask app'i deploy etmek için gerekli o yüzdne requirements içerisine de bunu ekledik.
* Ayrıca reqirements içerisinde direkt torch dersek, hem gpu hem cpu versions indirilir, boyutu çok büyük olur, heroku'da deploy edemeyiz. O yüzden requirements.txt içerisinde torch'u şu: şekilde import ettik:
 * -f https://download.pytorch.org/whl/torch_stable.html
   torch==1.6.0+cpu
   
 * Son olarak flask cors'u da import ettik ve flask app'imizin içinde bazı değişiklikler yaptık, bu sayede cors error almaktan kurtulduk, bunu yapmazsak, client ve api farklı domain'lerde olduğu için cors hatası alıyoruz.
