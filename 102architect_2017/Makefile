##
## EPITECH PROJECT, 2017
## Makefile
## File description:
##
##

SRC	=	./src/102architect.py	\

NAME	=	102architect

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 102architect.py
	mv 102architect.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
