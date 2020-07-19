from PIL import Image, ImageDraw, ImageFont

class create_image:
  def create_image_and_save(self, message, subreddit):
    if subreddit == "showerthoughts":
      img = Image.open("stock1.png")
    else:
      img = Image.open("monkeypaw.png")
    fnt = ImageFont.truetype('/Library/Fonts/Cocogoose-Classic-Medium-trial.ttf', 65)

    d = ImageDraw.Draw(img)
    d.text((165,450), message, font=fnt, fill=(0, 0, 0))

    img.save('pil_text_font2.png')
