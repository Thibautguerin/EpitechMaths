##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## makefile for transfer
##

SRC	=	./src/107transfer.py	\

NAME	=	107transfer

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 107transfer.py
	mv 107transfer.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
