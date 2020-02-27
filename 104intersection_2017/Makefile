##
## EPITECH PROJECT, 2017
## Makefile
## File description:
##
##

SRC	=	./src/104intersection.py	\

NAME	=	104intersection

all:	$(NAME)

$(NAME):	$(SRC)
	cp $(SRC) ./
	chmod +x 104intersection.py
	mv 104intersection.py $(NAME)

clean:
	rm -rf $(OBJ)

fclean: clean
	mv $(NAME) $(SRC)

re:	fclean all

auteur:
	echo $(USER) > auteur
