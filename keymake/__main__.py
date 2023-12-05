from keymake import resize_keep_aspect_ratio
from keymake import qpf, painter

try:
    import click
    from PIL import Image
    from PIL.GifImagePlugin import GifImageFile

except ImportError as e:
    errors = e
    print(f"please install the packages: {e}")
    raise


def green(text):
    return f"\033[92m{text}\033[00m"


def yellow(text):
    return f"\033[93m{text}\033[00m"


class Logger:
    def __init__(self, level):
        self.level = level

    def debug(self, message):
        if self.level:
            click.echo(f"[{green('oled-util')}][{yellow('DEBUG')}]:{message}")


class Context(object):
    def __init__(self, debug):
        self.debug = debug

    @property
    def logger(self):
        return Logger(level=self.debug)


@click.group()
@click.option('--debug/--no-debug', default=True, envvar='REPO_DEBUG')
@click.pass_context
def oled_utils(ctx, debug):
    """
    ModelOLED 圖片轉換 Command Line Interface.
    """
    ctx.obj = Context(debug=debug)
    ctx.obj.logger.debug("debug mode for oled-utils.")


@oled_utils.command()
@click.pass_obj
@click.argument('input_file', type=click.File('rb'))
def graphic_resize_format(ctx, input_file):
    """
    將圖片轉換成 64x48 pixel大小.
    """
    graphic = Image.open(input_file)
    ctx.logger.debug(input_file.name)

    extension = graphic.format.lower()
    output = open(
        f"{input_file.name.replace(f'.{extension}', '')}-resized.{extension}",
        "wb")
    resized_img = []
    for i in range(graphic.n_frames):
        graphic.seek(i)
        graphic.load()
        im = graphic.resize((int(graphic.size[0] * 0.95), graphic.size[1]),
                            Image.Resampling.LANCZOS)
        im = resize_keep_aspect_ratio(im, (64, 48))
        resized_img.append(im)
    resized_img[0].save(output, save_all=True, append_images=resized_img[1:])
    ctx.logger.debug(f"saved, path={output.name}")


@oled_utils.command()
@click.pass_obj
@click.argument('input_file', type=click.File('rb'))
@click.option('-d',
              '--deltas',
              type=bool,
              is_flag=True,
              default=False,
              show_default=False,
              help='Disables the use of delta frames when encoding animations.'
              )
def graphic2qgf(ctx, input_file, deltas):
    """
    轉換圖片至QGF(RGB252)檔案格式.
    """
    ctx.logger.debug(
        f"options, file_path={input_file.name}, deltas={deltas}")

    graphic = Image.open(input_file)

    extension = graphic.format.lower()
    output = open(f"{input_file.name.replace(f'.{extension}', '')}.qgf", "wb")
    graphic.save(output,
                 "QGF",
                 use_deltas=deltas,
                 use_rle=True,
                 qmk_format=painter.valid_formats["rgb565"])
    ctx.logger.debug(f"saved, path={output.name}")


if __name__ == "__main__":
    oled_utils()
