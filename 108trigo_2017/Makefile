##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## makefile for trigo
##

SRC	=	./src/108trigo.py	\

NAME	=	108trigo

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 108trigo.py
	mv 108trigo.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
