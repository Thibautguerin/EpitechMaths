##
## EPITECH PROJECT, 2017
## Makefile
## File description:
##
##

SRC	=	display_window.c	\

OBJ	=	$(SRC:.c=.o)

NAME	=	window

all:	$(NAME)

$(NAME):	$(SRC)
	gcc $(SRC)-o $(NAME) -l c_graph_prog

clean:
	rm -rf $(OBJ)

fclean: clean
	rm -rf $(NAME)

re:	fclean all

auteur:
	echo $(USER) > auteur
