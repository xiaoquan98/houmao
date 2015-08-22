run:
	python todo.py & echo $$! > "pid.tmp"

stop:
	kill -9 `cat pid.tmp`
	rm pid.tmp