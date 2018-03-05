using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;
using System.Windows.Forms;
using Tobii.Interaction;
using System.IO;


namespace experiment_eye
{
    public partial class Form1 : Form
    {

        private static Host _host;
        private static GazePointDataStream _gazePointDataStream;
        private static List<double> s1 = new List<double>();
        private static Label text = new Label();
        private static int[] size_s = { 2, 3, 4, 5, 6 };
        private static int press_key = 0;
        private static int count_chunk = 0;
        private static int[] chunks = new int[0];
        private static string[] sentences = File.ReadAllLines(@"C:test1.txt", Encoding.GetEncoding("iso-8859-1"));
        static Random _random = new Random();
        private static int count_key = 0;
        public static double time_st = 0;
        public static double init_st = 0;
        public static int fg = 0;
        public static double eye_x = 0;
        public static double eye_y = 0;
        public static bool bandtime = true;
        public static bool band = false;
        public static Bitmap img = new Bitmap(2560, 1440);
        public static Graphics g = Graphics.FromImage(img);
        public static string path = @"C:\Users\Inf-CG\Documents\images\";
        public Form1()
        {
           
            InitializeComponent();
            this.WindowState = FormWindowState.Maximized;
            //this.Size = img.Size;
            this.FormBorderStyle = FormBorderStyle.None;


            //this.BackgroundImage = img=;
            this.StartPosition = FormStartPosition.CenterScreen;
            //this.Size = new System.Drawing.Size(img.Width, img.Height);
            this.KeyPress += new KeyPressEventHandler(keypressed);
            Cursor.Hide();
        }

        static void Shuffle<T>(T[] array)
        {
            int n = array.Length;
            for (int i = 0; i < n; i++)
            {
                int r = i + _random.Next(n - i);
                T t = array[r];
                //Console.WriteLine(r.ToString() + "   " + array[r]);
                array[r] = array[i];
                array[i] = t;
                using (StreamWriter res = File.AppendText(@"C:\Users\Inf-CG\Google Drive\Bibliography- Span Test\sente.txt"))
                {
                    res.WriteLine(array[i] + "  " + r.ToString());
                }
            }
        }

        static int[] chunk()
        {

            int n = size_s.Sum();
            int m = sentences.Length;
            int es = m / n;
            List<int> temp = new List<int>();

            for (int i = 1; i <= m / n; i++)
            {
                Shuffle(size_s);
                foreach (int s in size_s)
                {
                    temp.Add(s);
                    using (StreamWriter sw = File.AppendText(@"C:\Users\Inf-CG\Documents\order.txt"))
                    {
                        sw.WriteLine(s.ToString());
                        //Console.WriteLine(s.ToString() + "  " + i.ToString() + "   " + (m/n).ToString());
                    }
                }
            }
            // foreach (int i in temp) {}
            return temp.ToArray();
        }

        private static void InitializeHost()
        {
            _host = new Host();
        }
        private static void DisableConnectionWithTobiiEngine()
        {
            _host.DisableConnection();
        }

        private static void CreateAndVisualizeLightlyFilteredGazePointStream()
        {
            _gazePointDataStream = _host.Streams.CreateGazePointDataStream();
            _gazePointDataStream.GazePoint((x, y, ts) =>
            {
                // Console.WriteLine("Timestamp: {0}\tX:{1}, Y:{2}", ts, x, y);
                s1.Add(ts);
                time_st = ts - s1[0];
                eye_x = x;
                eye_y = y;
                if (band)
                {
                    using (StreamWriter sw = File.AppendText(@"C:\Users\Inf-CG\Documents\raw_eye.txt"))
                    {
                        sw.WriteLine((ts - s1[0]).ToString("0.#").Replace(",", ".") + ";" + x.ToString("0.##").Replace(",", ".") + ";" + y.ToString("0.##").Replace(",", "."));
                    }
                }
            });
        }
        System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();

        private void Form1_Load(object sender, EventArgs e)
        {
            chunks = chunk();
            WindowState = FormWindowState.Maximized;
            text.Font = new Font("Arial", 50, FontStyle.Bold);
            Shuffle(sentences);
            text.Text = "Pressionar a tecla 'espaço' para começar." ;
            text.Size = this.Size;
            text.TextAlign = ContentAlignment.MiddleCenter;
       
           
            //PictureBox pbx = new PictureBox();
            //pbx.Image = img;
            //pbx.Size = this.Size;
            this.Controls.Add(text);
            timer.Tick += new EventHandler(timer_Tick);
            if (bandtime)
                timer.Interval = 7000;
            else
                timer.Interval = 1000000;

            // this.Controls.Add(pbx);
            //pbx.SizeMode = PictureBoxSizeMode.CenterImage;
            //pbx.SizeMode = PictureBoxSizeMode.StretchImage;
            //SetTimer();

            //keypressed(this,new KeyPressEventArgs f);
            InitializeHost();
            CreateAndVisualizeLightlyFilteredGazePointStream();
            //Console.WriteLine(timer_done);
            //  timer.Start();
        }
        private void keypressed(Object o, KeyPressEventArgs e)
        {
            // If the SPACE key is pressed, the Handled property is set to true, 
            // to indicate the event is handled.

            if (e.KeyChar == (char)Keys.Space)
            {
                g.CopyFromScreen(0, 0, 0, 0, img.Size);
                g.DrawImage(img, 0, 0, 0, 0);
                band = true;
                timer.Enabled = true;
                bandtime = true;
                timer.Stop();
                timer.Start();
                if (count_key < sentences.Length)
                {
                    //Console.WriteLine(count_chunk.ToString());

                    if (press_key == chunks[count_chunk])
                    {
                        text.Text = "+";
                        press_key = 0;
                        count_chunk++;
                        count_key--;
                        using (StreamWriter sw = File.AppendText(@"C:\Users\Inf-CG\Documents\rt.txt"))
                        {
                            sw.WriteLine(time_st.ToString("0.#").Replace(",", ".") + ";" + "0" + ";" + (time_st-init_st).ToString());
                        }
                        init_st = time_st;
                        timer.Stop();
                        timer.Enabled = false;
                        bandtime = false;
                    }
                    else if (press_key < chunks[count_chunk])
                    {
                        img.Save(path + @count_key.ToString() + @".png");
                        text.Text = sentences[count_key];
                        press_key++;
                        using (StreamWriter sw = File.AppendText(@"C:\Users\Inf-CG\Documents\rt.txt"))
                        {
                            sw.WriteLine(time_st.ToString("0.#").Replace(",", ".") + ";" + "1" + ";" + (time_st - init_st).ToString());
                        }
                        init_st = time_st;


                    }

                    //Console.WriteLine(press_key.ToString() + "  " + chunks[count_chunk].ToString() + "  " + count_key.ToString() + "  " + count_chunk.ToString());
                }
                else
                {
                    text.Text = "+";
                    fg++;
                    if (fg == 2)
                    {
                        this.Close();
                        DisableConnectionWithTobiiEngine();
                    }

                 
                }
                count_key++;
            }
            e.Handled = true;
        }


        void timer_Tick(object sender, EventArgs e)
        {
            if (count_key < sentences.Length)
            {
                g.CopyFromScreen(0, 0, 0, 0, img.Size);
                g.DrawImage(img, 0, 0, 0, 0);

                if (press_key == chunks[count_chunk])
                {
                    text.Text = "+";
                    press_key = 0;
                    count_chunk++;
                    count_key--;
                    using (StreamWriter sw = File.AppendText(@"C:rt.txt"))
                    {
                        sw.WriteLine(time_st.ToString("0.#").Replace(",", ".") + ";" + "0" + ";" + (time_st - init_st).ToString());
                    }
                    timer.Stop();
                    timer.Enabled = false;
                    bandtime = false;
                    init_st = time_st;

                }
                else if (press_key < chunks[count_chunk])
                {
                    img.Save(path + @count_key.ToString() + @".png");

                    text.Text = sentences[count_key];
                    press_key++;
                    using (StreamWriter sw = File.AppendText(@"C:rt.txt"))
                    {
                        sw.WriteLine(time_st.ToString("0.#").Replace(",", ".") + ";" + "1" + ";" + (time_st - init_st).ToString());
                    }
                    init_st = time_st;
                }

                // Console.WriteLine(press_key.ToString() + "  " + chunks[count_chunk].ToString() + "  " + count_key.ToString() + "  " + count_chunk.ToString());
            }
            else
            {
                text.Text = "+";
                fg++;
                if (fg == 2)
                {
                    this.Close();
                    DisableConnectionWithTobiiEngine();
                }
            }
            count_key++;
            ;// timer.Stop();
            //timer.Enabled = true;
            //this.Close();
            //DisableConnectionWithTobiiEngine();
            // ind++;
            //text.Text = d[ind
        }
    }
}
