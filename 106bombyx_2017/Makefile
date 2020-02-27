##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## makefile for bombyx
##

SRC	=	./src/106bombyx.py	\

NAME	=	106bombyx

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 106bombyx.py
	mv 106bombyx.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
