from pyChatGPT import ChatGPT
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="09128601494Sadra"
)

cur = conn.cursor()

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..hllIBnTxd1YjibHl.N1kAQHWgSS0TfzEaqtH2ZaoJBd9CM6B_SNcIjft5dkzw8z2icgaHz1vH6QtKhO1wbqFOtimk3abUD-3xtDlLdk08twKX-YbPOqV0brFswZ1Qda-b1hlkmtYic6mgPgtw6yq0R_XwM7FfM4IscZlA8LfEqwlF_Nvx77P9jw1XBAE9thv9FwDmEF-bX3-sRMWzNPWuJh2yr6A3jaXzLMaGm9GpScGcYnSTOrOO9ZMksCu50yANmEmiyDugcdaaXKV0WXLunPS1bqbqXKS5rbR3PbqVj3db2P3z1Tcf9nc9eBXcu5G_auCuAhvwRt5juerw_z9krf3YQYRJdOdCRXnmL8_d9gD7Se_ctGM8Rf8ec-59mbESRoeJcVzuFZaU4cpHAFTpyi5lxzbi_Fm_ZEbP8IxmY4MBwO6KgFkH-Ah1wRuFIWb2ipc1c6BLiDDrhVogq6VnsINO_AwnAliyLdX5Lee2yruOsny1_-tkXPdBnU8nTCSMPNBteVOYLXQCLWQ5r5ogNCzHUWduMeky4vDensObD6bX3bJ13b8XUz9xjq1ezwWaAd7YpJfk1GW1SzRO_nh2nt9rIPBFc_2QuOZP1lpPPpN8dbVRQsF5md1ZYp5cA2VleW6VGTp0qTKcBI_u7TAvbbvxseLBfXnOArJHrjqWsjJiaVdzlSr21OHfdpLnND_PuBVVHaA3fvBv2qObIVpkaDBf78b8DyrFUfOlgeusurJnxglh6XCd7seAddQYlJ3fQg_egNTXa-8mM9S32ImfkxbWr2ywiwq0FT7yTWqUwHenSpQ71u11N1rp8boj7pc2tzWVt_q469qkR4XYU8V_mDwny-yRG7AsftWgUZhCs59deg3e2Cp5CGXUiWNJNFOqo2hBdXsOEFIr2iUIRFmXK4yDbicb_KkzjaD9Ce9Zs18kZ986-jnlZOjf4XZwxvY1qgaoMP9YPD-GGV44-rG8BK1I8w8Fu__zdsZOxDzXsikDcwprGwGm8aoJZdi88MS-VHi0CkfvcajEN8n1dSN72FI8m_8q5CJaFossZE8mXNeiNs6w12lbITrbF10KZqf55azyWuiG2xagmvfucVVryvaJfrVD7G9lhixNBbC4PSdEECR9gfxVfwXSIi0CS8h8EMZymHuO_brwPAETr50ZHheuFGIAniagDY2miX4MFoYXmyI5mrWRlIgovwwfaUts_Zdhc0T70xGOnecgGOBcE5ymy7Z9XkQowZ25o-LREaK8_hObcNO7k-Q00D98FjheioxwVGdq74WFFWdAgB9RUVArKJAsPWolZgZkqWxHQa0HVTl5ZtVOmrlDnx1vXaw4YtawGZD8UfpdPYASVboO26TX0vg58Sc2fIY8AnRh3rWP6bwhXiAfn4chTMCSHgmdYnkEJmqmU_sJ4GcR4GCkFLo9yoRHtg7PHOZNeHkQT4WC0ZpeiGIaLnJSSq6sv9gmznn5E-1OupyQCGfeNhv70Fh7o07Z6k0Bow2kYYOYxQqStj85upvN61u0XF999zePgoTxdpqjyBdAYHneKbCLr_PDFBuHijbIlaKAE31ap_EljXGa-lf1sS3B2i7EgEY3f5gK1KQz4uGpC5pAu_MywA5nKf6jMZ0u7TpMwKoKD75nxgoYhQLAw4BSJIhcOaBhndG4eqWBkBLiB451nFjwiDBOPA2pscpUUQlbArQnWQwBJsQFTfX8urgo-FhUGYoEG0zINGvT6GbsTqN5Z2wq3CHhTcjSLy4T8yzRhTOlx_eZdRH7xZpOTrR2qADq9HcLE8ULUPTdirg6C79J3KNgytDobGB5fI1Z6d20suMy-gksZpd8TvJfPEak5f3BZADrT82_19TBnhp1yJclPRep-V7G_6AFxn5Ha7_RkJqbGrr6PPDDiN1u4BWDXA0l6ykT5-BhZkjELEC8eNDDiXk-5vp-ep7JFtnlkfRixtGtPKOd6QK0Piz-p5ZSldjPDqR-j1C9VKtRNXTfiBbKDurQUJPd-IW9Z7WqyVFCwqp3iHlakUL8hCpW7yDjALdWv85RSllOansSnZCKpsdfVC_iS_ScixC-ARxps0IhR7r762O9I2EXP22cj3TtgkaYjigmeql4pbj64Aj34tKEcfaErGWPXaMThpZzMthf6GyiQTzJAgCBNCMMGotiAJlIIMJZlAyPvqzeimhWB7Jyokf_10O_dvuY59Rd3FVRmwD_LNmN7zz3jwCIzHL1_SUYDlB3iIDoisZw2aa_BnYki4gsQRn_RR6DSxqmVTT52OMRH2zcKL0j_XVy9CtY4XIwG264ergMMzAn0C8KjfAKPaahOAnHKTElQe_gcw7nrR7W9U-4mbZ-a9G1CS4k05mqkoDewXGogGYvSrR7-gwFft91CQzQtNVoqNaFlcwQ85l6w6PkfaeqtjvM7a4wSth77TFMmk65Cl-QZ8jpAWENvr-a_fEMOs10mAzU9k7taxL1mRhTy_Coidl30W5DmXWbh78eTGoJTCN8wXhUHFyoY-JMbCdWWRI.FUCv1aGoUImXvXrx7vkt8Q'
api = ChatGPT(session_token)
cur.execute("SELECT id FROM people")
ids = cur.fetchall()
for id in ids:
    id = int(id[0])
    print(id)
    cur.execute("SELECT name FROM people WHERE id = {}".format(id))
    name = str(cur.fetchone())
    cur.execute("SELECT arm_length, chest_width FROM measurements WHERE person_id = {}".format(id))
    measurements = str(cur.fetchone())
    inp = 'make a personolized massage for' + name + 'with the measurments of arm length and chest width that they improved on' + measurements + 'senders name is dante'
    if inp == 'exit':
        break
    else:
        response = api.send_message(inp)
        massage = response['message']
        words = massage.split()
        smaller_lines = [words[i:i+10] for i in range(0, len(words), 10)]
        for line in smaller_lines:
            line_str = ' '.join(line)
            print(line_str)
