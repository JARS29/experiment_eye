using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
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
 
        
        private static string[] d = File.ReadAllLines(@"C:test.txt", Encoding.GetEncoding("iso-8859-1"));
        static Random _random = new Random();
        private static int ind = 0;
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
                array[r] = array[i];
                array[i] = t;
            }
        }

        static int[] chunk()
        {

            int n = size_s.Sum();
            int m = d.Length ;
            int es = m / n;
            Console.WriteLine(n.ToString() + " " + m.ToString() + " " + es.ToString());
            List<int> temp = new List<int>();

            for (int i = 0; i < m/n; i++)
            {
                Shuffle(size_s);
                foreach (int s in size_s) {temp.Add(s); }
            }
            Console.WriteLine(temp.Count().ToString());
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

                using (StreamWriter sw = File.AppendText(@"C:\Users\Inf-CG\Documents\WriteLines.txt"))
                {
                    sw.WriteLine((ts - s1[0]).ToString("0.#") + ";" + x.ToString("0.##") + ";" + y.ToString("0.##"));
                }
            });
        }
        //System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();
        private void Form1_Load(object sender, EventArgs e)
        {
            chunk();
            // Bitmap img = (Bitmap)Image.FromFile(@"C:\Users\Inf-CG\Downloads\123.png", true);
            WindowState = FormWindowState.Maximized;
            text.Font = new Font("Arial", 50, FontStyle.Bold);
            Shuffle(d);
            //text.Text = d[ind];
            text.Size = this.Size;
            text.TextAlign = ContentAlignment.MiddleCenter;
            //PictureBox pbx = new PictureBox();
            //pbx.Image = img;
            //pbx.Size = this.Size;
            this.Controls.Add(text);
            // this.Controls.Add(pbx);
            //pbx.SizeMode = PictureBoxSizeMode.CenterImage;
            //pbx.SizeMode = PictureBoxSizeMode.StretchImage;
            

           // timer.Interval = 5000;
            //keypressed(this,new KeyPressEventArgs f);
            InitializeHost();
            CreateAndVisualizeLightlyFilteredGazePointStream();
          //  timer.Tick += new EventHandler(timer_Tick);
          //  timer.Start();
        }
        private void keypressed(Object o, KeyPressEventArgs e)
    {
        
        // If the SPACE key is pressed, the Handled property is set to true, 
        // to indicate the event is handled.
        if (e.KeyChar == (char)Keys.Space)
        {

                if (ind < d.Length)
                {
                    text.Text = d[ind];
                }
                else
                {
                    this.Close();
                    DisableConnectionWithTobiiEngine();
                }
                }
            ind++;

            e.Handled = true;
    }

        //void timer_Tick(object sender, EventArgs e)
        //{
            //this.Close();
            //DisableConnectionWithTobiiEngine();
           // ind++;
            //text.Text = d[ind
        //}
    }
}
