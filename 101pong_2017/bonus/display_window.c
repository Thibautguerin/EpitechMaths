/*
** EPITECH PROJECT, 2017
** display_window.c
** File description:
** 
*/

#include <SFML/Graphics/RenderWindow.h>
#include <unistd.h>
#include <stdlib.h>
#include <SFML/Graphics/Sprite.h>
#include <SFML/Graphics/Texture.h>

int	main()
{
	sfRenderWindow *window;
	sfVideoMode video_mode;
	sfEvent *event;

	video_mode.width = 1600;
	video_mode.height = 900;
	video_mode.bitsPerPixel = 32;

	window = sfRenderWindow_create(video_mode, "PONG", sfClose, NULL);

	while (sfRenderWindow_isOpen(window)) {
		sfRenderWindow_display(window);
		while(sfRenderWindow_pollEvent(window, event)) {
			if (event->type == sfEvtClosed)
				sfRenderWindow_close(window);
		}
	}
	return (0);
}
