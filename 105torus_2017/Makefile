##
## EPITECH PROJECT, 2017
## Makefile
## File description:
##
##

SRC	=	./src/105torus.py	\

NAME	=	105torus

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 105torus.py
	mv 105torus.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
