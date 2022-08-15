import time
import random
from const import info_lightsabers, questions, answers
from pprint import pprint
import sys

def intro():
	'''Приветствие Йоды'''
	print('- Приветствую, тебя мой юный падаван.')
	time.sleep(2)
	print('- Световой меч твой сегодня цвет обретёт')
	time.sleep(3)
	print('- Многое цвет светового меча о его носителе рассказать может')
	time.sleep(3)
	print('- Узнать время пришло, какой стороне силы предпочтение ты отдаёшь.')
	time.sleep(3)
	print('- Вдумчиво на вопросы мои отвечать должен ты, чтобы истинный цвет меча своего узнать')
	time.sleep(3)
	print('- Ну что, начнём мы ?')
	time.sleep(2)

def pprint_question(questions, answers):
	'''Вывести вопрос с вариантами ответов'''
	question = questions.pop(random.randint(0, len(questions) - 1))
	print()
	print(question, '\n')
	variants = answers.pop(question)
	counter_vars = 1
	list_marks = []
	while len(variants) > 0:
		variant, marks = variants.pop(random.randint(0, len(variants) - 1))
		marks['index'] = counter_vars
		print('\t', counter_vars, ') ', variant, sep='')
		counter_vars += 1
		list_marks.append(marks)
	print()
	return list_marks

def input_answer(marks):
	'''Обработка пользовательского ввода и возврат его'''
	try:
		answer = int(input())
		if not 1 <= answer <= len(marks):
			raise IndexError
	except ValueError:
		print('Целое число вписать стоит тебе => ', end='')
		answer = input_answer(marks)
	except IndexError:
		print(f'Число от 1 до {len(marks)} впиши, юный падаван => ', end='')
		answer = input_answer(marks)
	except KeyboardInterrupt:
		print('Хмм... Видимо не сегодня цвет меча ты узнаешь...')
		sys.exit()
	finally:
		return answer
		print()

def recognise_answer(marks, answer):
	'''Возвращает правильную оценку ответа'''
	for mark in marks:
		if mark.pop('index') == answer:
			return mark

def change_counters(user_counters, correct_marks):
	'''Изменение пользовательских очков по его выбору'''
	for color, mark in correct_marks.items():
		user_counters[color] += mark
	return user_counters

def find_max(user_counters):
	max_mark = max(user_counters.values())
	colors = []
	for color in user_counters:
		if user_counters[color] == max_mark:
			colors.append(color)
	if len(colors) == 1:
		return colors[0]
	else:
		return colors

def main(questions, answers):
	'''Основной цикл вопросов проги'''
	user_counters = {'красный': 0, 'чёрный': 0, 'синий': 0, 'зелёный': 0, 'фиолетовый': 0, 'белый': 0, 'жёлтый': 0}
	while len(questions) > 0:
		all_marks = pprint_question(questions, answers)
		print('А здесь, падаван, ответ стоит вписать тебе (число перед вариантом ответа) => ', end='')
		answer = input_answer(all_marks)
		#answer = random.randint(1, len(all_marks))
		correct_marks = recognise_answer(all_marks, answer)
		user_counters = change_counters(user_counters, correct_marks)
	#print(user_counters)
	return find_max(user_counters)

def result(color_colors):
	'''Заключение, огласка результата'''
	time.sleep(2)
	print('...')
	time.sleep(2)
	print('- Хмм, к концу вопросы мои подошли')
	time.sleep(2)
	print('- И знаю теперь я много нового о тебе, мой друг')
	time.sleep(2)
	if type(color_colors) == str:
		print(f'- Цвет светового меча {color_colors} у тебя будет')
		time.sleep(2)
		give_info_sword(color_colors)
	else:
		print(f'- По моему мнению можешь ты выбрать либо {", либо ".join(color_colors)} световой меч.')
		time.sleep(2)
		for color in color_colors:
			give_info_sword(color)
		time.sleep(2)
		print('- Любой из них отлично сочитаться с тобою будет')
	time.sleep(2)
	print(f'- Прощай, падаван. Да прибудет с тобой сила !')
	time.sleep(2)

def give_info_sword(color):
	'''Выдаёт инфу о мече по цвету'''
	print()
	for sentence in info_lightsabers[color]:
		print(sentence)
		time.sleep(3.5)
	print()

if __name__ == '__main__':
	random.seed(time.time())
	intro()
	color_colors = main(questions, answers)
	#with open('result.txt', 'a', encoding='utf-8') as f:
	#	if type(color_colors) == str:
	#		f.write(color_colors + '\n')
	#	else:
	#		f.write(', '.join(color_colors) + '\n')
	result(color_colors)
	
