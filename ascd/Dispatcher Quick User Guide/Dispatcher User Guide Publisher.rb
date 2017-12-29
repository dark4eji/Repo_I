# Проверяем существует ли диск D.
drive = Dir.exist?('D:')

# ... и сразу задаём значение для переменной диска
if drive == true
    driveind = 'D:\\'
else
    driveind = 'C:\\'
end

# Задаём атрибуты использования кастомного шаблона и шрифтов + путь. Путь относительный.
fonts = ' -a pdf-fontsdir="..\System_files\sptt_fonts"'
template = ' -a pdf-style="..\System_files\sptt_pdf_template.yml"'

# Объявляем переменную для цикла приёма ответа.
language = 0

# Цикл приёма ответа. Соответственно, если введённый ответ не совпадает
# с нужным, то будет выводится сообщение после else и петля повторяется.
loop do
# Вывод вопроса
  print("Enter the desired language[eng/rus/pt]: ")
# Приём ответа
  input = gets.chomp
  # Проверка введённого ответа и назначение языка
  if input == "eng"
    language = 'EN'
	break
  elsif input == "rus"
    language = 'RU'
	break
  else puts 'Try another' # Значение false возвращающее цикл в начало
  end  
end

# Собираем переменную конченой папки
output_folder = "#{driveind}PUBLISHED\\Asc_#{language}"

# Собираем переменную до файла-ток-проекта
mainpath = "'#{language}\\Dispatcher Quick User Guide.adoc'"

# Обращаемся к ОС окружению и публикуем файл
system "asciidoctor-pdf -D #{output_folder} #{mainpath}"

# Пауза для просмотра лога
sleep
