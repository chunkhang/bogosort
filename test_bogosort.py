#!/usr/bin/env python3

import sys; sys.path.append('../bogosort')
from bogosort import bogosort

def test_prompt_numbers_valid(capfd, monkeypatch):
	for i in ['1 2', '1 2 3', '10 4 50  1', '1  1 1   1']:
		monkeypatch.setitem(__builtins__, 'input', lambda x: i)
		p = 'Prompt'
		e = 'Error'
		bogosort._promptNumbers(prompt=p, error=e, test=True)
		out, err = capfd.readouterr()
		assert out == p + '\n'

def test_prompt_numbers_invalid(capfd, monkeypatch):
	for i in ['Apple', 'a b', '1, 2, 3', '1 2 a', '1 2, 3', '42']:
		monkeypatch.setitem(__builtins__, 'input', lambda x: i)
		p = 'Prompt'
		e = 'Error'
		bogosort._promptNumbers(prompt=p, error=e, test=True)
		out, err = capfd.readouterr()
		assert out == p + '\n' + e+'\n' + '\n'

def test_is_sorted_true():
	assert bogosort._isSorted([1, 2, 3]) == True
	assert bogosort._isSorted([1, 1, 1, 2, 3, 3]) == True

def test_is_sorted_false():
	assert bogosort._isSorted([2, 1, 3]) == False
	assert bogosort._isSorted([2, 3, 4, 3]) == False

def test_format_shuffles_single_to_hundred():
	assert bogosort._formatShuffles(0) == '0'
	assert bogosort._formatShuffles(10) == '10'
	assert bogosort._formatShuffles(142) == '142'

def test_format_shuffles_thousand_to_hundred_thousand():
	assert bogosort._formatShuffles(1066) == '1,066'
	assert bogosort._formatShuffles(12333) == '12,333'
	assert bogosort._formatShuffles(999999) == '999,999'

def test_format_shuffles_million_to_hundred_million():	
	assert bogosort._formatShuffles(1000000) == '1,000,000'
	assert bogosort._formatShuffles(10000000) == '10,000,000'
	assert bogosort._formatShuffles(100000000) == '100,000,000'

def test_format_time_seconds():
	assert bogosort._formatTime(0.4901) == '0s'
	assert bogosort._formatTime(0.5001) == '1s'
	assert bogosort._formatTime(58.9) == '59s'

def test_format_time_minutes_seconds():
	assert bogosort._formatTime(60.49) == '1m 0s'
	assert bogosort._formatTime(121) == '2m 1s'
	assert bogosort._formatTime(3599) == '59m 59s'

def test_format_time_hours_minutes_seconds():
	assert bogosort._formatTime(3600.1) == '1h 0m 0s'
	assert bogosort._formatTime(3720) == '1h 2m 0s'
	assert bogosort._formatTime(10000000) == '2777h 46m 40s'