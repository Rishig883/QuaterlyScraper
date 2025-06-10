import os
import logging
import builtins

from Saudi.saudiUrlExtractor import Saudi_urls
from Saudi.saudiProfileScraper import Saudi_profiles

from Bahrain.bahrainUrlExtractor import bahrain_urls
from Bahrain.bahrainProfileScraper import bahrain_pdfs

from Kuwait.kuwaitUrlExtractor import kuwait_urls
from Kuwait.kuwaitProfileScraper import kuwait_pdfs

from Qe.qeUrlExtractor import qe_pdfs

from Dubai.dubaiProfileScraper import dubai_pdfs
from Dubai.dubaiUrlExtractor import dubai_urls

from Oman.omanProfileScraper import oman_pdfs
from Oman.omanUrlScraper import oman_urls

from Adx.adxProfileScraper import adx_pdfs

from pdfDownloader import download_pdfs_from_csv
from pdfNamingExact import rename_pdfs_from_csv
from pdfNamingLatest import download_pdfs_by_latest
from unzipper import unzip
from sendFile import send_financial_reports

# --- Create logs directory ---
os.makedirs("logs", exist_ok=True)

# --- Logging configuration ---
logging.basicConfig(
    filename='logs/application.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- Override print to log only ---
def print(*args, **kwargs):
    message = " ".join(str(arg) for arg in args)
    logging.info(message)

# --- Main application logic ---
def main():
    year = input("Year: ")
    quarter = input("Quarter: ")
    print(f"Starting PDF extraction for {year}/Q{quarter}...")
    suffix = f"_{year}_Q{quarter}.pdf"

    print("Starting Saudi URL extraction...")
    Saudi_urls()
    Saudi_profiles(quarter=quarter, year=year)
    download_pdfs_from_csv(csv_path='saudi.csv',output_folder=f'FinancialReports/saudi/{year}/Q{quarter}',wait_time=20)
    rename_pdfs_from_csv(csv_file_path='saudi.csv',pdf_folder_path=f'FinancialReports/saudi/{year}/Q{quarter}',suffix=suffix)
    send_financial_reports(file = 'saudi.csv', destination = f'FinancialReports/saudi/{year}/Q{quarter}' )


    print("Starting Bahrain URL extraction...")
    bahrain_urls('bahrainUrls.csv')
    bahrain_pdfs('bahrainUrls.csv', 'bahrain.csv', year=year, quarter=quarter)
    download_pdfs_from_csv(csv_path='bahrain.csv', output_folder=f'FinancialReports/bahrain/{year}/Q{quarter}')
    rename_pdfs_from_csv(csv_file_path='bahrain.csv', pdf_folder_path=f'FinancialReports/bahrain/{year}/Q{quarter}', suffix=suffix)
    send_financial_reports(file = 'bahrain.csv', destination = f'FinancialReports/bahrain/{year}/Q{quarter}' )


    print("Starting Kuwait URL extraction...")
    kuwait_urls('kuwaitUrls.csv')  
    kuwait_pdfs('kuwaitUrls.csv', 'kuwait.csv', year=year, quarter=quarter)
    download_pdfs_from_csv(csv_path='kuwait.csv', output_folder=f'FinancialReports/kuwait/{year}/Q{quarter}')
    rename_pdfs_from_csv(csv_file_path='kuwait.csv', pdf_folder_path=f'FinancialReports/kuwait/{year}/Q{quarter}', suffix=suffix)
    send_financial_reports(file = 'kuwait.csv', destination = f'FinancialReports/kuwait/{year}/Q{quarter}' )



    print("Starting Dubai URL extraction...")
    dubai_urls() 
    dubai_pdfs(year=year, quarter=quarter)
    download_pdfs_from_csv(csv_path='dubai.csv', output_folder=f'FinancialReports/dubai/{year}/Q{quarter}')
    rename_pdfs_from_csv(csv_file_path='dubai.csv', pdf_folder_path=f'FinancialReports/dubai/{year}/Q{quarter}', suffix=suffix)
    send_financial_reports(file = 'dubai.csv', destination = f'FinancialReports/dubai/{year}/Q{quarter}' )



    print("Starting Qe URL extraction...")
    qe_pdfs(year=year, quarter=int(quarter))
    download_pdfs_by_latest('qeUrls.csv', suffix=suffix, download_folder=f'FinancialReports/Qatar/{year}/Q{quarter}')
    send_financial_reports(file = 'qeUrls.csv', destination = f'FinancialReports/Qatar/{year}/Q{quarter}' )



    print("Starting Oman URL extraction...")
    oman_urls()
    oman_pdfs(year=year, quarter=quarter)
    download_pdfs_from_csv(csv_path='oman.csv', output_folder=f'FinancialReports/oman/{year}/Q{quarter}')
    unzip(folder_path=f'FinancialReports/oman/{year}/Q{quarter}')
    send_financial_reports(file = 'oman.csv', destination = f'FinancialReports/oman/{year}/Q{quarter}' )


    print("Starting ADX URL extraction...")
    adx_pdfs(year=year, quarter=quarter)
    download_pdfs_from_csv(csv_path='adx.csv', output_folder=f'FinancialReports/AbuDhabi/{year}/Q{quarter}')
    rename_pdfs_from_csv(csv_file_path='adx.csv', pdf_folder_path=f'FinancialReports/AbuDhabi/{year}/Q{quarter}', suffix=suffix)
    send_financial_reports(file = 'adx.csv', destination = f'FinancialReports/AbuDhabi/{year}/Q{quarter}' )

if __name__ == "__main__":
    main()
