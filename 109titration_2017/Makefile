##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## makefile for titration
##

SRC	=	./src/109titration.py	\

NAME	=	109titration

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 109titration.py
	mv 109titration.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
