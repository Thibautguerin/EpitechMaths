##
## EPITECH PROJECT, 2017
## Makefile
## File description:
##
##

SRC	=	./src/103cipher.py	\

NAME	=	103cipher

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 103cipher.py
	mv 103cipher.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
