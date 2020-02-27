##
## EPITECH PROJECT, 2017
## Makefile
## File description:
##
##

SRC	=	./src/101pong.py	\

NAME	=	101pong

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 101pong.py
	mv 101pong.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
