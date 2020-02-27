##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## makefile for borwein
##

SRC	=	./src/110borwein.py	\

NAME	=	110borwein

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 110borwein.py
	mv 110borwein.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
