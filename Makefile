next-day:
	@read -p "Enter day directory: " day_directory; \
	mkdir -p $$day_directory; \
	touch $$day_directory/__init__.py; \
	touch $$day_directory/input.txt; \
	cp default_script.py $$day_directory/script.py; \
	touch $$day_directory/test.py;
