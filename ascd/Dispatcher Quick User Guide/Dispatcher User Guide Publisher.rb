# Проверяем существует ли диск D.
drive = Dir.exist?('D:')

# ... и сразу задаём значение для переменной диска
if drive == true
    driveind = 'D:\\'
else
    driveind = 'C:\\'
end

# Задаём атрибуты использования кастомного шаблона и шрифтов + путь. Путь относительный.
fonts_path = ' -a pdf-fontsdir="..\System_files\sptt_fonts"'
pdf_template_path = ' -a pdf-style="..\System_files\sptt_pdf_template.yml"'
css_template_path = ' -a stylesheet="..\..\System_files\chm_style.css"'

# Объявление переменных циклов
language = "none"
doctype = "none"

# Цикл приёма ответа. Соответственно, если введённый ответ не совпадает
# с нужным, то будет выводиться сообщение после else и петля повторяется.
loop do
# Вывод вопроса
  print("Enter the desired language[en/ru/pt]: ")

# Приём ответа
  language = gets.chomp
  language = language.upcase

  # Проверка введённого ответа и назначение конечного значения переменной языка
  if language == "EN" || language == "RU" || language == "PT"
    break
  else
    puts 'Please, try again' # Значение false возвращающее цикл в начало
  end
end

loop do

  print("Enter the doc type[pdf/html]: ")
  doctype = gets.chomp
  doctype = doctype.upcase

  if doctype == "PDF"
    doctype = "asciidoctor-pdf"
	css_template_path = ''
    break

  elsif doctype == "HTML"
    doctype = "asciidoctor"
	fonts_path = ''
	pdf_template_path = ''

    loop do
        print "Use the default html theme?[yes/no]: "
        answer = gets.chomp
        answer = answer.upcase

        if answer == "YES"
          css_template_path = ''
          break
		  
        elsif answer == "NO"
          break
		  
        else 'Please, try again'
        end
     end
    break

  else
    puts 'Please, try again'
  end
end

# Собираем переменную папки выгрузки
output_folder = "#{driveind}PUBLISHED\\Asc_#{language}"

# Собираем переменную пути к файлу ток/проекта
mainpath = "'#{language}\\Dispatcher Quick User Guide.adoc'"
add_attrs = "#{fonts_path} #{pdf_template_path} #{css_template_path}"

# Обращаемся к ОС окружению и публикуем файл
#system "asciidoctor-pdf -D #{output_folder} #{add_attrs} #{mainpath}"
system "#{doctype} -D #{output_folder} #{add_attrs} #{mainpath}"

# Пауза для просмотра лога
sleep
